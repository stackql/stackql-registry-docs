---
title: operationalization_clusters_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - operationalization_clusters_keys
  - ml_compute
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operationalization_clusters_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_compute.operationalization_clusters_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="appInsights" /> | `object` | AppInsights credentials. |
| <CopyableCode code="containerRegistry" /> | `object` | Information about the Azure Container Registry which contains the images deployed to the cluster. |
| <CopyableCode code="containerService" /> | `object` | Information about the Azure Container Registry which contains the images deployed to the cluster. |
| <CopyableCode code="serviceAuthConfiguration" /> | `object` | Global service auth configuration properties. These are the data-plane authorization keys and are used if a service doesn't define it's own. |
| <CopyableCode code="sslConfiguration" /> | `object` | SSL configuration. If configured data-plane calls to user services will be exposed over SSL only. |
| <CopyableCode code="storageAccount" /> | `object` | Access information for the storage account. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> |
