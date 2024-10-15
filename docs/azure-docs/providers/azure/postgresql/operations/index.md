---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - postgresql
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the operation being performed on this particular object. |
| <CopyableCode code="display" /> | `object` | Display metadata associated with the operation. |
| <CopyableCode code="isDataAction" /> | `boolean` | Indicates whether the operation is a data action |
| <CopyableCode code="origin" /> | `string` | The intended executor of the operation. |
| <CopyableCode code="properties" /> | `object` | Additional descriptions for the operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all of the available REST API operations. |
| <CopyableCode code="check_migration_name_availability" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, targetDbServerName, data__name, data__type" /> | This method checks whether a proposed migration name is valid and available. |
| <CopyableCode code="check_name_availability_execute" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Check the availability of name for resource |
| <CopyableCode code="check_name_availability_with_location_execute" /> | `EXEC` | <CopyableCode code="locationName, subscriptionId" /> | Check the availability of name for resource |

## `SELECT` examples

Lists all of the available REST API operations.


```sql
SELECT
name,
display,
isDataAction,
origin,
properties
FROM azure.postgresql.operations
;
```