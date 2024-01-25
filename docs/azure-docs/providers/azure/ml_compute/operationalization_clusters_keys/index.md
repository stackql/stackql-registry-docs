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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operationalization_clusters_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ml_compute.operationalization_clusters_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `appInsights` | `object` | AppInsights credentials. |
| `containerRegistry` | `object` | Information about the Azure Container Registry which contains the images deployed to the cluster. |
| `containerService` | `object` | Information about the Azure Container Registry which contains the images deployed to the cluster. |
| `serviceAuthConfiguration` | `object` | Global service auth configuration properties. These are the data-plane authorization keys and are used if a service doesn't define it's own. |
| `sslConfiguration` | `object` | SSL configuration. If configured data-plane calls to user services will be exposed over SSL only. |
| `storageAccount` | `object` | Access information for the storage account. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` |
