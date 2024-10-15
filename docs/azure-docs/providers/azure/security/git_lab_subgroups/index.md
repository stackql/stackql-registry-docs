---
title: git_lab_subgroups
hide_title: false
hide_table_of_contents: false
keywords:
  - git_lab_subgroups
  - security
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

Creates, updates, deletes, gets or lists a <code>git_lab_subgroups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>git_lab_subgroups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.git_lab_subgroups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | GitLab Group properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupFQName, resourceGroupName, securityConnectorName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
properties,
systemData
FROM azure.security.git_lab_subgroups
WHERE groupFQName = '{{ groupFQName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND securityConnectorName = '{{ securityConnectorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```