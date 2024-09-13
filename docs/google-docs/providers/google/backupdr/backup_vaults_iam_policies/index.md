---
title: backup_vaults_iam_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_vaults_iam_policies
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

Creates, updates, deletes, gets or lists a <code>backup_vaults_iam_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_vaults_iam_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.backupdr.backup_vaults_iam_policies" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="test_iam_permissions" /> | `EXEC` | <CopyableCode code="backupVaultsId, locationsId, projectsId" /> | Returns the caller's permissions on a BackupVault resource. A caller is not required to have Google IAM permission to make this request. |
