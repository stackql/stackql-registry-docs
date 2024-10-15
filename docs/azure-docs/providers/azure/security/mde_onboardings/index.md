---
title: mde_onboardings
hide_title: false
hide_table_of_contents: false
keywords:
  - mde_onboardings
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

Creates, updates, deletes, gets or lists a <code>mde_onboardings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mde_onboardings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.mde_onboardings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Properties of the MDE configuration or data parameter needed to onboard the machine to MDE |
| <CopyableCode code="type" /> | `string` | Resource type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The default configuration or data needed to onboard the machine to MDE |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The configuration or data needed to onboard the machine to MDE |

## `SELECT` examples

The default configuration or data needed to onboard the machine to MDE


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.mde_onboardings
WHERE subscriptionId = '{{ subscriptionId }}';
```