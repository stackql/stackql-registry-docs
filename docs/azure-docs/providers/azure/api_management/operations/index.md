---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - api_management
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="api" /> | `object` | API contract properties for the Tag Resources. |
| <CopyableCode code="operation" /> | `object` | Operation Entity contract Properties. |
| <CopyableCode code="product" /> | `object` | Product profile. |
| <CopyableCode code="tag" /> | `object` | Contract defining the Tag property in the Tag Resource Contract |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all of the available REST API operations of the Microsoft.ApiManagement provider. |
| <CopyableCode code="list_by_tags" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of operations associated with tags. |
| <CopyableCode code="perform_connectivity_check_async" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, data__destination, data__source" /> | Performs a connectivity check between the API Management service and a given destination, and returns metrics for the connection, as well as errors encountered while trying to establish it. |

## `SELECT` examples

Lists all of the available REST API operations of the Microsoft.ApiManagement provider.


```sql
SELECT
api,
operation,
product,
tag
FROM azure.api_management.operations
;
```