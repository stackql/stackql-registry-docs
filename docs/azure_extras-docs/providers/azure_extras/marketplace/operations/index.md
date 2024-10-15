---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - marketplace
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.marketplace.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Operation ID |
| <CopyableCode code="name" /> | `string` | Operation name: {provider}/{resource}/{operation} |
| <CopyableCode code="display" /> | `object` | The object that represents the operation. |
| <CopyableCode code="isDataAction" /> | `boolean` | Indicates whether the operation is a data action |
| <CopyableCode code="origin" /> | `string` | Origin of the operation |
| <CopyableCode code="properties" /> | `object` | Operation properties. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all of the available Microsoft.Marketplace REST API operations. |
| <CopyableCode code="query_rules" /> | `EXEC` | <CopyableCode code="collectionId, privateStoreId" /> | Get a list of all private store rules in the given private store and collection |
| <CopyableCode code="query_user_rules" /> | `EXEC` | <CopyableCode code="privateStoreId" /> | All rules approved in the private store that are relevant for user subscriptions |
| <CopyableCode code="set_collection_rules" /> | `EXEC` | <CopyableCode code="collectionId, privateStoreId" /> | Set rule for specific private store and collection |

## `SELECT` examples

Lists all of the available Microsoft.Marketplace REST API operations.


```sql
SELECT
id,
name,
display,
isDataAction,
origin,
properties
FROM azure_extras.marketplace.operations
;
```