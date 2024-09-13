---
title: resources
hide_title: false
hide_table_of_contents: false
keywords:
  - resources
  - config
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

Creates, updates, deletes or gets an <code>resource</code> resource or lists <code>resources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.config.resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name. Format: `projects/{project}/locations/{location}/deployments/{deployment}/revisions/{revision}/resources/{resource}` |
| <CopyableCode code="caiAssets" /> | `object` | Output only. Map of Cloud Asset Inventory (CAI) type to CAI info (e.g. CAI ID). CAI type format follows https://cloud.google.com/asset-inventory/docs/supported-asset-types |
| <CopyableCode code="intent" /> | `string` | Output only. Intent of the resource. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the resource. |
| <CopyableCode code="terraformInfo" /> | `object` | Terraform info of a Resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deploymentsId, locationsId, projectsId, resourcesId, revisionsId" /> | Gets details about a Resource deployed by Infra Manager. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deploymentsId, locationsId, projectsId, revisionsId" /> | Lists Resources in a given revision. |

## `SELECT` examples

Lists Resources in a given revision.

```sql
SELECT
name,
caiAssets,
intent,
state,
terraformInfo
FROM google.config.resources
WHERE deploymentsId = '{{ deploymentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND revisionsId = '{{ revisionsId }}'; 
```
