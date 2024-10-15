---
title: disk_encryption_sets_associated_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_encryption_sets_associated_resources
  - compute
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

Creates, updates, deletes, gets or lists a <code>disk_encryption_sets_associated_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disk_encryption_sets_associated_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.disk_encryption_sets_associated_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="diskEncryptionSetName, resourceGroupName, subscriptionId" /> | Lists all resources that are encrypted with this disk encryption set. |

## `SELECT` examples

Lists all resources that are encrypted with this disk encryption set.


```sql
SELECT
column_anon
FROM azure.compute.disk_encryption_sets_associated_resources
WHERE diskEncryptionSetName = '{{ diskEncryptionSetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```