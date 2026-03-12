class Leafdb {
  #url; // (encapsulating url)

  constructor() {
    this.#url = `http://localhost:8000`;
  }
  /* Sets the port used in the uvicorn server */
  setPort(port) {
    if (!(typeof port === "number")) {
      throw new SyntaxError(`Invalid port: ${port}`);
    }
    this.#url = `http://localhost:${port}`;
  }
  /**
   * Returns an object with the database data
   * @param {number} data optional argument, if specified, returns that specific item, otherwise returns all the database
   */
  async view(data = null) {
    if (data) {
      const rawContent = await fetch(`${this.#url}/${data}`);
      if (!rawContent.ok) {
        throw new Error(`${rawContent.status} ${rawContent.statusText}`);
      }
      const content = await rawContent.json();
      return content;
    }

    const rawContent = await fetch(this.#url);
    if (!rawContent.ok) {
      throw new Error(`${rawContent.status} ${rawContent.statusText}`);
    }
    const content = await rawContent.json();
    return content;
  }
  /* Deletes `item` from the database */
  async del(item) {

    const data = await new Leafdb().view();
    if (!Object.keys(data).includes(item)) {
      console.warn(`${item} isn't found in database`);
      return;
    }

    const res = await fetch(`${this.#url}/${item}`, {
      method: "DELETE",
    });

    if (!res.ok) {
      throw new Error(`${res.status} ${res.statusText}`);
    }
  }
  /* Inserts `data` to the database */
  async insert(data) {
    if (!(data instanceof Object) || data === null || Array.isArray(data)) {
      throw new TypeError(`Invalid structure: ${data}`);
    }

    const res = await fetch(this.#url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    if (!res.ok) {
      throw new Error(`${res.status} ${res.statusText}`);
    }
  }
  /* Changes `key`'s value to `value` in the database */
  async edit(key, value) {
    if (key === null || Array.isArray(key)) {
      throw new TypeError(`Invalid structure: ${key}`);
    }

    const res = await fetch(`${this.#url}/${key}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ value }),
    });

    if (!res.ok) {
      throw new Error(`${res.status} ${res.statusText}`);
    }
  }

  /* Provides read-only access to the URL */
  getUrl() {
    return this.#url;
  }
}
export default Leafdb;
