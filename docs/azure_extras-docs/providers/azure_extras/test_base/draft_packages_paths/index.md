---
title: draft_packages_paths
hide_title: false
hide_table_of_contents: false
keywords:
  - draft_packages_paths
  - test_base
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

Creates, updates, deletes, gets or lists a <code>draft_packages_paths</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>draft_packages_paths</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.draft_packages_paths" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="baseUrl" /> | `string` | The base URL of the storage account. |
| <CopyableCode code="draftPackagePath" /> | `string` | The relative path of the folder hosting package files. |
| <CopyableCode code="expirationTime" /> | `string` | Expiry date of the SAS token. |
| <CopyableCode code="sasToken" /> | `string` | A SAS token for the storage account to access workspace. |
| <CopyableCode code="workingPath" /> | `string` | The relative path for a temporary folder for package creation work. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets draft package path and temp working path with SAS. |

## `SELECT` examples

Gets draft package path and temp working path with SAS.


```sql
SELECT
baseUrl,
draftPackagePath,
expirationTime,
sasToken,
workingPath
FROM azure_extras.test_base.draft_packages_paths
WHERE draftPackageName = '{{ draftPackageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```