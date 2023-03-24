# StackQL Doc Autogeneration

Used to generate markdown docs for stackql providers using provider metadata from the [StackQL Provider Registry](https://github.com/stackql/stackql-provider-registry).  

## Setup

Add or update the required provider metadata to [docgen/provider_data.py](https://github.com/stackql/registry.stackql.io/blob/main/scripts/docgen/provider_data.py).

## Usage

```bash
sh docgen.sh <provider>
```

for example...  

```bash
sh docgen.sh google
```

This command would generate the docs for the `v23.01.00116` version of the `google` StackQL provider, the docs would be created in the `docs/google` folder, once they are verified the docs can be moved to `/docs/providers/google`.  

