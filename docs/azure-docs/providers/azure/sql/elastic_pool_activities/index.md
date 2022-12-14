---
title: elastic_pool_activities
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_pool_activities
  - sql
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
<tr><td><b>Name</b></td><td><code>elastic_pool_activities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.elastic_pool_activities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Represents the properties of an elastic pool. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ElasticPoolActivities_ListByElasticPool` | `SELECT` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` |
