# StackQL Doc Autogeneration

Used to generate markdown docs for stackql providers using provider metadata from the [StackQL Provider Registry](https://github.com/stackql/stackql-provider-registry).  

## Steps

1. Run the prequisite steps (to download the latest `stackql` binary for linux along with the `pystackql` Python package), run the following command:

```bash
sh ./docgen_prereqs.sh
```

2. Add the necessary provider level metadata to [docgen/provider_data.py](https://github.com/stackql/registry.stackql.io/blob/main/scripts/docgen/provider_data.py).  

3. Run the following command to generate the markdown docs:

```bash
python3 docgen/generate_docs.py <provider> <version>
```

for example...  

```bash
python3 docgen/generate_docs.py azure v0.3.0
python3 docgen/generate_docs.py aws v0.1.3
```

This command would generate the docs for the `v0.3.0` version of the `azure` StackQL provider, the docs would be created in the `docs/azure` folder, once they are verified the docs can be moved to `/docs/providers/azure`.  

The [stackql-provider-registry.md](https://github.com/stackql/registry.stackql.io/blob/main/docs/stackql-provider-registry.md) page should be updated as well to include a tile for `azure`.  

