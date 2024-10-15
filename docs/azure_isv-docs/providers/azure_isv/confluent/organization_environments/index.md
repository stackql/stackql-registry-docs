---
title: organization_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_environments
  - confluent
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

Creates, updates, deletes, gets or lists a <code>organization_environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organization_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.confluent.organization_environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the environment |
| <CopyableCode code="name" /> | `string` | Display name of the environment |
| <CopyableCode code="kind" /> | `string` | Type of environment |
| <CopyableCode code="properties" /> | `object` | Environment resource property |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
id,
name,
kind,
properties
FROM azure_isv.confluent.organization_environments
WHERE organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```