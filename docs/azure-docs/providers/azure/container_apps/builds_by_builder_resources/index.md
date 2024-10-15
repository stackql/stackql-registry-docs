---
title: builds_by_builder_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - builds_by_builder_resources
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>builds_by_builder_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>builds_by_builder_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.builds_by_builder_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The build properties. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="builderName, resourceGroupName, subscriptionId" /> | List BuildResource resources by BuilderResource |

## `SELECT` examples

List BuildResource resources by BuilderResource


```sql
SELECT
properties
FROM azure.container_apps.builds_by_builder_resources
WHERE builderName = '{{ builderName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```