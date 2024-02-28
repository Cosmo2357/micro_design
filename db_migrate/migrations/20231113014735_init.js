/**
 * @param { import("knex").Knex } knex
 * @returns { Promise<void> }
 */

exports.up = function (knex) {
  return (
    knex.schema
      .createTable("users", (table) => {
        table.increments("id").primary();
        table.string("display_name", 255).notNullable();
        table.text("bio");
        table.json("metadata");
        table.timestamps(true, true);
      })
  );
};

// in db folder
// knex migrate:down
// knex migrate:up

// knex seed:run

/* /**
 * @param { import("knex").Knex } knex
 * @returns { Promise<void> }
 */
exports.down = function (knex) {
  return knex.schema
    .dropTableIfExists("users")
};

