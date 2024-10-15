---
title: container_host_mappings_container_host_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - container_host_mappings_container_host_mappings
  - dev_spaces
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

Creates, updates, deletes, gets or lists a <code>container_host_mappings_container_host_mappings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_host_mappings_container_host_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.dev_spaces.container_host_mappings_container_host_mappings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="containerHostResourceId" /> | `string` | ARM ID of the Container Host resource |
| <CopyableCode code="mappedControllerResourceId" /> | `string` | ARM ID of the mapped Controller resource |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
containerHostResourceId,
mappedControllerResourceId
FROM azure_extras.dev_spaces.container_host_mappings_container_host_mappings
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```