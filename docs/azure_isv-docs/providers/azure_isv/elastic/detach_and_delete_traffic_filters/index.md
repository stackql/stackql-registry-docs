---
title: detach_and_delete_traffic_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - detach_and_delete_traffic_filters
  - elastic
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

Creates, updates, deletes, gets or lists a <code>detach_and_delete_traffic_filters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>detach_and_delete_traffic_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.elastic.detach_and_delete_traffic_filters" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |  |

## `DELETE` example

Deletes the specified <code>detach_and_delete_traffic_filters</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.elastic.detach_and_delete_traffic_filters
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
