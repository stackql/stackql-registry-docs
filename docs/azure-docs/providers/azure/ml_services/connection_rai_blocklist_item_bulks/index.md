---
title: connection_rai_blocklist_item_bulks
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_rai_blocklist_item_bulks
  - ml_services
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

Creates, updates, deletes, gets or lists a <code>connection_rai_blocklist_item_bulks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connection_rai_blocklist_item_bulks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.connection_rai_blocklist_item_bulks" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionName, raiBlocklistName, resourceGroupName, subscriptionId, workspaceName" /> |  |

## `DELETE` example

Deletes the specified <code>connection_rai_blocklist_item_bulks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.ml_services.connection_rai_blocklist_item_bulks
WHERE connectionName = '{{ connectionName }}'
AND raiBlocklistName = '{{ raiBlocklistName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
