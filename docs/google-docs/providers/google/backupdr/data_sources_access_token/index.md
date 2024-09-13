
---
title: data_sources_access_token
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources_access_token
  - backupdr
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

Creates, updates, deletes or gets an <code>data_sources_access_token</code> resource or lists <code>data_sources_access_token</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sources_access_token</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.backupdr.data_sources_access_token" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="expireTime" /> | `string` | The token is valid until this time. |
| <CopyableCode code="readLocation" /> | `string` | The location in bucket that can be used for reading. |
| <CopyableCode code="token" /> | `string` | The downscoped token that was created. |
| <CopyableCode code="writeLocation" /> | `string` | The location in bucket that can be used for writing. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_access_token" /> | `SELECT` | <CopyableCode code="backupVaultsId, dataSourcesId, locationsId, projectsId" /> | Internal only. Fetch access token for a given data source. |

## `SELECT` examples

Internal only. Fetch access token for a given data source.

```sql
SELECT
expireTime,
readLocation,
token,
writeLocation
FROM google.backupdr.data_sources_access_token
WHERE backupVaultsId = '{{ backupVaultsId }}'
AND dataSourcesId = '{{ dataSourcesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
