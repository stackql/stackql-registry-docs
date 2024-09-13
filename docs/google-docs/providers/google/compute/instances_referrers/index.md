
---
title: instances_referrers
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_referrers
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

Creates, updates, deletes or gets an <code>instances_referrer</code> resource or lists <code>instances_referrers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_referrers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.instances_referrers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#reference for references. |
| <CopyableCode code="referenceType" /> | `string` | A description of the reference type with no implied semantics. Possible values include: 1. MEMBER_OF  |
| <CopyableCode code="referrer" /> | `string` | URL of the resource which refers to the target. |
| <CopyableCode code="target" /> | `string` | URL of the resource to which this reference points. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_referrers" /> | `SELECT` | <CopyableCode code="instance, project, zone" /> | Retrieves a list of resources that refer to the VM instance specified in the request. For example, if the VM instance is part of a managed or unmanaged instance group, the referrers list includes the instance group. For more information, read Viewing referrers to VM instances. |

## `SELECT` examples

Retrieves a list of resources that refer to the VM instance specified in the request. For example, if the VM instance is part of a managed or unmanaged instance group, the referrers list includes the instance group. For more information, read Viewing referrers to VM instances.

```sql
SELECT
kind,
referenceType,
referrer,
target
FROM google.compute.instances_referrers
WHERE instance = '{{ instance }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}'; 
```
