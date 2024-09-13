
---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
  - securitycenter
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

Creates, updates, deletes or gets an <code>asset</code> resource or lists <code>assets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.assets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="asset" /> | `object` | Security Command Center representation of a Google Cloud resource. The Asset is a Security Command Center resource that captures information about a single Google Cloud resource. All modifications to an Asset are only within the context of Security Command Center and don't affect the referenced Google Cloud resource. |
| <CopyableCode code="stateChange" /> | `string` | State change of the asset between the points in time. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_assets_list" /> | `SELECT` | <CopyableCode code="foldersId" /> | Lists an organization's assets. |
| <CopyableCode code="organizations_assets_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists an organization's assets. |
| <CopyableCode code="projects_assets_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists an organization's assets. |
| <CopyableCode code="folders_assets_group" /> | `EXEC` | <CopyableCode code="foldersId" /> | Filters an organization's assets and groups them by their specified properties. |
| <CopyableCode code="organizations_assets_group" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Filters an organization's assets and groups them by their specified properties. |
| <CopyableCode code="organizations_assets_run_discovery" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Runs asset discovery. The discovery is tracked with a long-running operation. This API can only be called with limited frequency for an organization. If it is called too frequently the caller will receive a TOO_MANY_REQUESTS error. |
| <CopyableCode code="projects_assets_group" /> | `EXEC` | <CopyableCode code="projectsId" /> | Filters an organization's assets and groups them by their specified properties. |

## `SELECT` examples

Lists an organization's assets.

```sql
SELECT
asset,
stateChange
FROM google.securitycenter.assets
WHERE foldersId = '{{ foldersId }}'; 
```
