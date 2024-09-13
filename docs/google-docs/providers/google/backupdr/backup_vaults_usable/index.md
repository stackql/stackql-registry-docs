---
title: backup_vaults_usable
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_vaults_usable
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

Creates, updates, deletes, gets or lists a <code>backup_vaults_usable</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_vaults_usable</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.backupdr.backup_vaults_usable" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="backupVaults" /> | `array` | The list of BackupVault instances in the project for the specified location. If the '{location}' value in the request is "-", the response contains a list of instances from all locations. In case any location is unreachable, the response will only return backup vaults in reachable locations and the 'unreachable' field will be populated with a list of unreachable locations. |
| <CopyableCode code="nextPageToken" /> | `string` | A token identifying a page of results the server should return. |
| <CopyableCode code="unreachable" /> | `array` | Locations that could not be reached. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_usable" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | FetchUsableBackupVaults lists usable BackupVaults in a given project and location. Usable BackupVault are the ones that user has backupdr.backupVaults.get permission. |

## `SELECT` examples

FetchUsableBackupVaults lists usable BackupVaults in a given project and location. Usable BackupVault are the ones that user has backupdr.backupVaults.get permission.

```sql
SELECT
backupVaults,
nextPageToken,
unreachable
FROM google.backupdr.backup_vaults_usable
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
