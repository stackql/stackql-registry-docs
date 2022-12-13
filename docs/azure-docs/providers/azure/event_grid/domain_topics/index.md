---
title: domain_topics
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_topics
  - event_grid
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
<tr><td><b>Name</b></td><td><code>domain_topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.domain_topics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier of the resource. |
| `name` | `string` | Name of the resource. |
| `properties` | `object` | Properties of the Domain Topic. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DomainTopics_Get` | `SELECT` | `domainName, domainTopicName, resourceGroupName, subscriptionId` | Get properties of a domain topic. |
| `DomainTopics_ListByDomain` | `SELECT` | `domainName, resourceGroupName, subscriptionId` | List all the topics in a domain. |
| `DomainTopics_CreateOrUpdate` | `INSERT` | `domainName, domainTopicName, resourceGroupName, subscriptionId` | Asynchronously creates or updates a new domain topic with the specified parameters. |
| `DomainTopics_Delete` | `DELETE` | `domainName, domainTopicName, resourceGroupName, subscriptionId` | Delete existing domain topic. |
