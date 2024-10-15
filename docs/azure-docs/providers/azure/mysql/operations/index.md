---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - mysql
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the operation being performed on this particular object. |
| <CopyableCode code="display" /> | `object` | Display metadata associated with the operation. |
| <CopyableCode code="origin" /> | `string` | The intended executor of the operation. |
| <CopyableCode code="properties" /> | `object` | Additional descriptions for the operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all of the available REST API operations. |
| <CopyableCode code="check_name_availability_execute" /> | `EXEC` | <CopyableCode code="locationName, subscriptionId, data__name" /> | Check the availability of name for server |
| <CopyableCode code="check_name_availability_without_location_execute" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name" /> | Check the availability of name for server |
| <CopyableCode code="check_virtual_network_subnet_usage_execute" /> | `EXEC` | <CopyableCode code="locationName, subscriptionId" /> | Get virtual network subnet usage for a given vNet resource id. |

## `SELECT` examples

Lists all of the available REST API operations.


```sql
SELECT
name,
display,
origin,
properties
FROM azure.mysql.operations
;
```