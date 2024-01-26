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
 Provision, manage, and integrate independent software vendor services on Azure.  
    
:::info Provider Summary (v24.01.00199)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>20</b></span><br />
<span>total methods:&nbsp;<b>906</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>253</b></span><br />
<span>total selectable resources:&nbsp;<b>246</b></span><br />
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


StackQL uses Azure application credentials obtained using the `az login` command from the Azure SDK.  For more information, see [here](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli).

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
<a href="/providers/azure_isv/logz/">logz</a><br />
<a href="/providers/azure_isv/netapp/">netapp</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/azure_isv/newrelic/">newrelic</a><br />
<a href="/providers/azure_isv/nginx/">nginx</a><br />
<a href="/providers/azure_isv/paloaltonetworks/">paloaltonetworks</a><br />
<a href="/providers/azure_isv/qumulo/">qumulo</a><br />
<a href="/providers/azure_isv/redhat_openshift/">redhat_openshift</a><br />
<a href="/providers/azure_isv/redis/">redis</a><br />
<a href="/providers/azure_isv/redis_enterprise/">redis_enterprise</a><br />
<a href="/providers/azure_isv/sap_workloads/">sap_workloads</a><br />
<a href="/providers/azure_isv/vmware/">vmware</a><br />
<a href="/providers/azure_isv/vmware_cloud_simple/">vmware_cloud_simple</a><br />
</div>
</div>
