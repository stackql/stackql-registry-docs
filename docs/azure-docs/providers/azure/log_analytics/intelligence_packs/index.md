---
title: intelligence_packs
hide_title: false
hide_table_of_contents: false
keywords:
  - intelligence_packs
  - log_analytics
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

Creates, updates, deletes, gets or lists a <code>intelligence_packs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>intelligence_packs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.intelligence_packs" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Lists all the intelligence packs possible and whether they are enabled or disabled for a given workspace. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="intelligencePackName, resourceGroupName, subscriptionId, workspaceName" /> | Disables an intelligence pack for a given workspace. |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="intelligencePackName, resourceGroupName, subscriptionId, workspaceName" /> | Enables an intelligence pack for a given workspace. |

## `SELECT` examples

Lists all the intelligence packs possible and whether they are enabled or disabled for a given workspace.


```sql
SELECT

FROM azure.log_analytics.intelligence_packs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```