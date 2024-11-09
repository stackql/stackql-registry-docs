---
title: confluent
hide_title: false
hide_table_of_contents: false
keywords:
  - confluent
  - kafka
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Confluent Cloud resources using SQL
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
id: confluent-doc
slug: /providers/confluent

---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Confluent Cloud for managing Kafka clusters, topics, and streaming services in a scalable cloud environment.


:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>22</b></span><br />
<span>total resources:&nbsp;<b>132</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `confluent` provider, run the following command:  

```bash
REGISTRY PULL confluent;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

The following system environment variables are used for authentication by default:  

- <CopyableCode code="CONFLUENT_CLOUD_API_KEY" /> - Confluent Cloud API key (see <a href="https://docs.confluent.io/cloud/current/security/authenticate/overview.html#api-keys">Confluent Cloud API Keys</a>)
- <CopyableCode code="CONFLUENT_CLOUD_API_SECRET" /> - Confluent Cloud API secret (see <a href="https://docs.confluent.io/cloud/current/security/authenticate/overview.html#api-keys">Confluent Cloud API Keys</a>)
        
These variables are sourced at runtime (from the local machine or as CI variables/secrets).  

<details>

<summary>Using different environment variables</summary>

To use different environment variables (instead of the defaults), use the `--auth` flag of the `stackql` program.  For example:  

```bash

AUTH='{ "confluent": { "type": "basic", "username_var": "MY_CONFLUENT_CLOUD_API_KEY_VAR", "password_var": "MY_CONFLUENT_CLOUD_API_SECRET_VAR" }}'
stackql shell --auth="${AUTH}"
        
```

or using PowerShell:  

```powershell

$Auth = "{ 'confluent': { 'type': 'basic', 'username_var': 'MY_CONFLUENT_CLOUD_API_KEY_VAR', 'password_var': 'MY_CONFLUENT_CLOUD_API_SECRET_VAR' }}"
stackql.exe shell --auth=$Auth
        
```
</details>


## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/confluent/billing/">billing</a><br />
<a href="/providers/confluent/catalog/">catalog</a><br />
<a href="/providers/confluent/connect/">connect</a><br />
<a href="/providers/confluent/encryption_keys/">encryption_keys</a><br />
<a href="/providers/confluent/flink_artifacts/">flink_artifacts</a><br />
<a href="/providers/confluent/flink_compute_pools/">flink_compute_pools</a><br />
<a href="/providers/confluent/iam/">iam</a><br />
<a href="/providers/confluent/kafka/">kafka</a><br />
<a href="/providers/confluent/ksqldb_clusters/">ksqldb_clusters</a><br />
<a href="/providers/confluent/managed_kafka_clusters/">managed_kafka_clusters</a><br />
<a href="/providers/confluent/networking/">networking</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/confluent/notifications/">notifications</a><br />
<a href="/providers/confluent/org/">org</a><br />
<a href="/providers/confluent/partner/">partner</a><br />
<a href="/providers/confluent/pipelines/">pipelines</a><br />
<a href="/providers/confluent/provider_integrations/">provider_integrations</a><br />
<a href="/providers/confluent/quotas/">quotas</a><br />
<a href="/providers/confluent/schema_registry/">schema_registry</a><br />
<a href="/providers/confluent/schema_registry_clusters/">schema_registry_clusters</a><br />
<a href="/providers/confluent/sql/">sql</a><br />
<a href="/providers/confluent/stream_sharing/">stream_sharing</a><br />
<a href="/providers/confluent/sts/">sts</a><br />
</div>
</div>
