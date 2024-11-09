---
title: azure
hide_title: false
hide_table_of_contents: false
keywords:
  - azure
  - microsoft azure
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
id: azure-doc
slug: /providers/azure

---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Core cloud services from Microsoft Azure.

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

To pull the latest version of the `azure` provider, run the following command:  

```bash
REGISTRY PULL azure;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

StackQL uses Azure application credentials obtained using the <CopyableCode code="az login" /> command from the Azure SDK.  For more information, see <a href="https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli">here</a>.

### Authenticating using an Azure Service Principal

To authenticate using an Azure Service Principal, set the following environment variables: <CopyableCode code="AZURE_TENANT_ID" />, <CopyableCode code="AZURE_CLIENT_ID" /> and <CopyableCode code="AZURE_CLIENT_SECRET" />, see [__creating-an-azure-service-principal__](https://learn.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication-service-principal?tabs=azure-cli#2-create-an-azure-service-principal).

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
