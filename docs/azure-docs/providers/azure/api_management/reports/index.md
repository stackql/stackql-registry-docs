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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.reports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name depending on report endpoint specifies product, API, operation or developer name. |
| <CopyableCode code="apiId" /> | `string` | API identifier path. /apis/&#123;apiId&#125; |
| <CopyableCode code="apiRegion" /> | `string` | API region identifier. |
| <CopyableCode code="apiTimeAvg" /> | `number` | Average time it took to process request. |
| <CopyableCode code="apiTimeMax" /> | `number` | Maximum time it took to process request. |
| <CopyableCode code="apiTimeMin" /> | `number` | Minimum time it took to process request. |
| <CopyableCode code="bandwidth" /> | `integer` | Bandwidth consumed. |
| <CopyableCode code="cacheHitCount" /> | `integer` | Number of times when content was served from cache policy. |
| <CopyableCode code="cacheMissCount" /> | `integer` | Number of times content was fetched from backend. |
| <CopyableCode code="callCountBlocked" /> | `integer` | Number of calls blocked due to invalid credentials. This includes calls returning HttpStatusCode.Unauthorized and HttpStatusCode.Forbidden and HttpStatusCode.TooManyRequests |
| <CopyableCode code="callCountFailed" /> | `integer` | Number of calls failed due to gateway or backend errors. This includes calls returning HttpStatusCode.BadRequest(400) and any Code between HttpStatusCode.InternalServerError (500) and 600 |
| <CopyableCode code="callCountOther" /> | `integer` | Number of other calls. |
| <CopyableCode code="callCountSuccess" /> | `integer` | Number of successful calls. This includes calls returning HttpStatusCode &lt;= 301 and HttpStatusCode.NotModified and HttpStatusCode.TemporaryRedirect |
| <CopyableCode code="callCountTotal" /> | `integer` | Total number of calls. |
| <CopyableCode code="country" /> | `string` | Country to which this record data is related. |
| <CopyableCode code="interval" /> | `string` | Length of aggregation period.  Interval must be multiple of 15 minutes and may not be zero. The value should be in ISO 8601 format (http://en.wikipedia.org/wiki/ISO_8601#Durations). |
| <CopyableCode code="operationId" /> | `string` | Operation identifier path. /apis/&#123;apiId&#125;/operations/&#123;operationId&#125; |
| <CopyableCode code="productId" /> | `string` | Product identifier path. /products/&#123;productId&#125; |
| <CopyableCode code="region" /> | `string` | Country region to which this record data is related. |
| <CopyableCode code="serviceTimeAvg" /> | `number` | Average time it took to process request on backend. |
| <CopyableCode code="serviceTimeMax" /> | `number` | Maximum time it took to process request on backend. |
| <CopyableCode code="serviceTimeMin" /> | `number` | Minimum time it took to process request on backend. |
| <CopyableCode code="subscriptionId" /> | `string` | Subscription identifier path. /subscriptions/&#123;subscriptionId&#125; |
| <CopyableCode code="timestamp" /> | `string` | Start of aggregation period. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| <CopyableCode code="userId" /> | `string` | User identifier path. /users/&#123;userId&#125; |
| <CopyableCode code="zip" /> | `string` | Zip code to which this record data is related. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="$filter, resourceGroupName, serviceName, subscriptionId" /> | Lists report records by subscription. |
| <CopyableCode code="list_by_api" /> | `EXEC` | <CopyableCode code="$filter, resourceGroupName, serviceName, subscriptionId" /> | Lists report records by API. |
| <CopyableCode code="list_by_geo" /> | `EXEC` | <CopyableCode code="$filter, resourceGroupName, serviceName, subscriptionId" /> | Lists report records by geography. |
| <CopyableCode code="list_by_operation" /> | `EXEC` | <CopyableCode code="$filter, resourceGroupName, serviceName, subscriptionId" /> | Lists report records by API Operations. |
| <CopyableCode code="list_by_product" /> | `EXEC` | <CopyableCode code="$filter, resourceGroupName, serviceName, subscriptionId" /> | Lists report records by Product. |
| <CopyableCode code="list_by_request" /> | `EXEC` | <CopyableCode code="$filter, resourceGroupName, serviceName, subscriptionId" /> | Lists report records by Request. |
| <CopyableCode code="list_by_time" /> | `EXEC` | <CopyableCode code="$filter, interval, resourceGroupName, serviceName, subscriptionId" /> | Lists report records by Time. |
| <CopyableCode code="list_by_user" /> | `EXEC` | <CopyableCode code="$filter, resourceGroupName, serviceName, subscriptionId" /> | Lists report records by User. |
