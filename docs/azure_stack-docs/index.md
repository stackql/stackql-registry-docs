---
title: azure_stack
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_stack
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
id: azure_stack-doc
slug: /providers/azure_stack
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Build and run hybrid apps across datacenters, edge locations, remote offices, and the cloud.  

:::info Provider Summary (v24.10.00256)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>18</b></span><br />
<span>total resources:&nbsp;<b>173</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `azure_stack` provider, run the following command:  

```bash
REGISTRY PULL azure_stack;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

StackQL uses Azure application credentials obtained using the <CopyableCode code="az login" /> command from the Azure SDK.  For more information, see <a href="https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli">here</a>.

### Authenticating using an Azure Service Principal

To authenticate using an Azure Service Principal, set the following environment variables: <CopyableCode code="AZURE_TENANT_ID" />, <CopyableCode code="AZURE_CLIENT_ID" /> and <CopyableCode code="AZURE_CLIENT_SECRET" />, see [__creating-an-azure-service-principal__](https://learn.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication-service-principal?tabs=azure-cli#2-create-an-azure-service-principal).

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/azure_stack/azure_bridge_admin/">azure_bridge_admin</a><br />
<a href="/providers/azure_stack/azure_stack/">azure_stack</a><br />
<a href="/providers/azure_stack/azure_stack_hci/">azure_stack_hci</a><br />
<a href="/providers/azure_stack/backup_admin/">backup_admin</a><br />
<a href="/providers/azure_stack/commerce_admin/">commerce_admin</a><br />
<a href="/providers/azure_stack/compute_admin/">compute_admin</a><br />
<a href="/providers/azure_stack/container_registry_admin/">container_registry_admin</a><br />
<a href="/providers/azure_stack/container_service_admin/">container_service_admin</a><br />
<a href="/providers/azure_stack/deployment_admin/">deployment_admin</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/azure_stack/fabric_admin/">fabric_admin</a><br />
<a href="/providers/azure_stack/gallery_admin/">gallery_admin</a><br />
<a href="/providers/azure_stack/infrastructure_insights_admin/">infrastructure_insights_admin</a><br />
<a href="/providers/azure_stack/key_vault_admin/">key_vault_admin</a><br />
<a href="/providers/azure_stack/network_admin/">network_admin</a><br />
<a href="/providers/azure_stack/storage_admin/">storage_admin</a><br />
<a href="/providers/azure_stack/subscriptions_admin/">subscriptions_admin</a><br />
<a href="/providers/azure_stack/update_admin/">update_admin</a><br />
<a href="/providers/azure_stack/user_subscriptions/">user_subscriptions</a><br />
</div>
</div>
