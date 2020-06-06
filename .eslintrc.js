/** @type {import('@types/eslint').Linter.Config} */
module.exports = {
  parser: "@typescript-eslint/parser",
  plugins: ["jest", "@typescript-eslint", "prettier", "github"],
  extends: [
    "eslint:recommended",
    "plugin:@typescript-eslint/eslint-recommended",
    "plugin:@typescript-eslint/recommended",
    "prettier/@typescript-eslint",
    "plugin:prettier/recommended",
    "plugin:github/recommended",
  ],
  rules: {
    "import/no-namespace": "off",
    "require-await": "error",
    "no-return-await": "warn",
  },
  env: {
    node: true,
    es6: true,
  },
}
