
---
title: error_frames
hide_title: false
hide_table_of_contents: false
keywords:
  - error_frames
  - migrationcenter
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

Creates, updates, deletes or gets an <code>error_frame</code> resource or lists <code>error_frames</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>error_frames</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.migrationcenter.error_frames" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The identifier of the ErrorFrame. |
| <CopyableCode code="ingestionTime" /> | `string` | Output only. Frame ingestion time. |
| <CopyableCode code="originalFrame" /> | `object` | Contains data reported from an inventory source on an asset. |
| <CopyableCode code="violations" /> | `array` | Output only. All the violations that were detected for the frame. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="errorFramesId, locationsId, projectsId, sourcesId" /> | Gets the details of an error frame. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, sourcesId" /> | Lists all error frames in a given source and location. |

## `SELECT` examples

Lists all error frames in a given source and location.

```sql
SELECT
name,
ingestionTime,
originalFrame,
violations
FROM google.migrationcenter.error_frames
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND sourcesId = '{{ sourcesId }}'; 
```
