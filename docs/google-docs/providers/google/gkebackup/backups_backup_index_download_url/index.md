---
title: backups_backup_index_download_url
hide_title: false
hide_table_of_contents: false
keywords:
  - backups_backup_index_download_url
  - gkebackup
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

Creates, updates, deletes or gets an <code>backups_backup_index_download_url</code> resource or lists <code>backups_backup_index_download_url</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups_backup_index_download_url</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.gkebackup.backups_backup_index_download_url" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="signedUrl" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_backup_index_download_url" /> | `SELECT` | <CopyableCode code="backupPlansId, backupsId, locationsId, projectsId" /> | Retrieve the link to the backupIndex. |

## `SELECT` examples

Retrieve the link to the backupIndex.

```sql
SELECT
signedUrl
FROM google.gkebackup.backups_backup_index_download_url
WHERE backupPlansId = '{{ backupPlansId }}'
AND backupsId = '{{ backupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
