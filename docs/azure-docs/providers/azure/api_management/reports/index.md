---
title: reports
hide_title: false
hide_table_of_contents: false
keywords:
  - reports
  - api_management
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
<tr><td><b>Name</b></td><td><code>reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.reports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name depending on report endpoint specifies product, API, operation or developer name. |
| `apiId` | `string` | API identifier path. /apis/&#123;apiId&#125; |
| `apiRegion` | `string` | API region identifier. |
| `apiTimeAvg` | `number` | Average time it took to process request. |
| `apiTimeMax` | `number` | Maximum time it took to process request. |
| `apiTimeMin` | `number` | Minimum time it took to process request. |
| `bandwidth` | `integer` | Bandwidth consumed. |
| `cacheHitCount` | `integer` | Number of times when content was served from cache policy. |
| `cacheMissCount` | `integer` | Number of times content was fetched from backend. |
| `callCountBlocked` | `integer` | Number of calls blocked due to invalid credentials. This includes calls returning HttpStatusCode.Unauthorized and HttpStatusCode.Forbidden and HttpStatusCode.TooManyRequests |
| `callCountFailed` | `integer` | Number of calls failed due to gateway or backend errors. This includes calls returning HttpStatusCode.BadRequest(400) and any Code between HttpStatusCode.InternalServerError (500) and 600 |
| `callCountOther` | `integer` | Number of other calls. |
| `callCountSuccess` | `integer` | Number of successful calls. This includes calls returning HttpStatusCode &lt;= 301 and HttpStatusCode.NotModified and HttpStatusCode.TemporaryRedirect |
| `callCountTotal` | `integer` | Total number of calls. |
| `country` | `string` | Country to which this record data is related. |
| `interval` | `string` | Length of aggregation period.  Interval must be multiple of 15 minutes and may not be zero. The value should be in ISO 8601 format (http://en.wikipedia.org/wiki/ISO_8601#Durations). |
| `operationId` | `string` | Operation identifier path. /apis/&#123;apiId&#125;/operations/&#123;operationId&#125; |
| `productId` | `string` | Product identifier path. /products/&#123;productId&#125; |
| `region` | `string` | Country region to which this record data is related. |
| `serviceTimeAvg` | `number` | Average time it took to process request on backend. |
| `serviceTimeMax` | `number` | Maximum time it took to process request on backend. |
| `serviceTimeMin` | `number` | Minimum time it took to process request on backend. |
| `subscriptionId` | `string` | Subscription identifier path. /subscriptions/&#123;subscriptionId&#125; |
| `timestamp` | `string` | Start of aggregation period. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `userId` | `string` | User identifier path. /users/&#123;userId&#125; |
| `zip` | `string` | Zip code to which this record data is related. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_subscription` | `SELECT` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by subscription. |
| `_list_by_api` | `EXEC` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by API. |
| `_list_by_geo` | `EXEC` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by geography. |
| `_list_by_operation` | `EXEC` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by API Operations. |
| `_list_by_product` | `EXEC` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by Product. |
| `_list_by_request` | `EXEC` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by Request. |
| `_list_by_subscription` | `EXEC` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by subscription. |
| `_list_by_time` | `EXEC` | `$filter, interval, resourceGroupName, serviceName, subscriptionId` | Lists report records by Time. |
| `_list_by_user` | `EXEC` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by User. |
| `list_by_api` | `EXEC` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by API. |
| `list_by_geo` | `EXEC` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by geography. |
| `list_by_operation` | `EXEC` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by API Operations. |
| `list_by_product` | `EXEC` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by Product. |
| `list_by_request` | `EXEC` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by Request. |
| `list_by_time` | `EXEC` | `$filter, interval, resourceGroupName, serviceName, subscriptionId` | Lists report records by Time. |
| `list_by_user` | `EXEC` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by User. |
