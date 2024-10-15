---
title: azure_isv
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_isv
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
id: azure_isv-doc
slug: /providers/azure_isv
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Provision, manage, and integrate independent software vendor services on Azure.  

:::info Provider Summary (v24.10.00256)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>23</b></span><br />
<span>total resources:&nbsp;<b>307</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `azure_isv` provider, run the following command:  

```bash
REGISTRY PULL azure_isv;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

StackQL uses Azure application credentials obtained using the <CopyableCode code="az login" /> command from the Azure SDK.  For more information, see <a href="https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli">here</a>.

### Authenticating using an Azure Service Principal

To authenticate using an Azure Service Principal, set the following environment variables: <CopyableCode code="AZURE_TENANT_ID" />, <CopyableCode code="AZURE_CLIENT_ID" /> and <CopyableCode code="AZURE_CLIENT_SECRET" />, see [__creating-an-azure-service-principal__](https://learn.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication-service-principal?tabs=azure-cli#2-create-an-azure-service-principal).

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/azure_isv/astro/">astro</a><br />
<a href="/providers/azure_isv/confluent/">confluent</a><br />
<a href="/providers/azure_isv/connected_vsphere/">connected_vsphere</a><br />
<a href="/providers/azure_isv/databricks/">databricks</a><br />
<a href="/providers/azure_isv/datadog/">datadog</a><br />
<a href="/providers/azure_isv/dynatrace/">dynatrace</a><br />
<a href="/providers/azure_isv/elastic/">elastic</a><br />
<a href="/providers/azure_isv/hana_on_azure/">hana_on_azure</a><br />
<a href="/providers/azure_isv/informatica/">informatica</a><br />
<a href="/providers/azure_isv/logz/">logz</a><br />
<a href="/providers/azure_isv/mongo_db/">mongo_db</a><br />
<a href="/providers/azure_isv/netapp/">netapp</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/azure_isv/newrelic/">newrelic</a><br />
<a href="/providers/azure_isv/nginx/">nginx</a><br />
<a href="/providers/azure_isv/openshift_clusters/">openshift_clusters</a><br />
<a href="/providers/azure_isv/oracle/">oracle</a><br />
<a href="/providers/azure_isv/paloalto/">paloalto</a><br />
<a href="/providers/azure_isv/redis/">redis</a><br />
<a href="/providers/azure_isv/redis_enterprise/">redis_enterprise</a><br />
<a href="/providers/azure_isv/sap_workloads/">sap_workloads</a><br />
<a href="/providers/azure_isv/split/">split</a><br />
<a href="/providers/azure_isv/vmware/">vmware</a><br />
<a href="/providers/azure_isv/vmware_cloud_simple/">vmware_cloud_simple</a><br />
</div>
</div>
