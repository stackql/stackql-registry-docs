# StackQL Doc Autogeneration

Used to generate markdown docs for stackql providers using provider metadata from the [StackQL Provider Registry](https://github.com/stackql/stackql-provider-registry).  

## Setup

Add or update the required provider metadata to [docgen/provider_data.py](https://github.com/stackql/registry.stackql.io/blob/main/scripts/docgen/provider_data.py).  

Download the latest version:  

```bash
curl -L https://bit.ly/stackql-zip -O \
&& unzip stackql-zip
```

## Usage

```bash
sh docgen.sh <provider>
```

for example...  

```bash
sh docgen.sh google
```

This command would generate the docs for the `latest` version of the `google` StackQL provider, the docs would be created in the `docs/google` folder, once they are verified the docs can be moved to `/docs/providers/google`.  

> if you wanted to generate docs for a specific version you could provide that version as the second argument, for example:
> `sh docgen.sh google v23.03.00130`

## Publishing Docs

Once the docs have been generated and verified they can be published to `docs` dir at the root of this project by running the following command:

```bash
sh publish.sh <provider>
```

for example...  

```bash
sh publish.sh google
```
