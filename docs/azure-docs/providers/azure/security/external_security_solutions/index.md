---
title: external_security_solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - external_security_solutions
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

Creates, updates, deletes, gets or lists a <code>external_security_solutions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>external_security_solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.external_security_solutions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="kind" /> | `string` | The kind of the external solution |
| <CopyableCode code="location" /> | `string` | Location where the resource is stored |
| <CopyableCode code="type" /> | `string` | Resource type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ascLocation, externalSecuritySolutionsName, resourceGroupName, subscriptionId" /> | Gets a specific external Security Solution. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of external security solutions for the subscription. |
| <CopyableCode code="list_by_home_region" /> | `SELECT` | <CopyableCode code="ascLocation, subscriptionId" /> | Gets a list of external Security Solutions for the subscription and location. |

## `SELECT` examples

Gets a list of external security solutions for the subscription.


```sql
SELECT
id,
name,
kind,
location,
type
FROM azure.security.external_security_solutions
WHERE subscriptionId = '{{ subscriptionId }}';
```