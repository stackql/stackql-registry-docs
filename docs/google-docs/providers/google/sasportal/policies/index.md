
---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - sasportal
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

Creates, updates, deletes or gets an <code>policy</code> resource or lists <code>policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sasportal.policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="assignments" /> | `array` | List of assignments |
| <CopyableCode code="etag" /> | `string` | The etag is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. It is strongly suggested that systems make use of the etag in the read-modify-write cycle to perform policy updates in order to avoid race conditions: An etag is returned in the response to GetPolicy, and systems are expected to put that etag in the request to SetPolicy to ensure that their change will be applied to the same version of the policy. If no etag is provided in the call to GetPolicy, then the existing policy is overwritten blindly. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="policies_get" /> | `SELECT` | <CopyableCode code="" /> | Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |
| <CopyableCode code="policies_set" /> | `EXEC` | <CopyableCode code="" /> | Sets the access control policy on the specified resource. Replaces any existing policy. |
| <CopyableCode code="policies_test" /> | `EXEC` | <CopyableCode code="" /> | Returns permissions that a caller has on the specified resource. |

## `SELECT` examples

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

```sql
SELECT
assignments,
etag
FROM google.sasportal.policies
WHERE  = '{{  }}'; 
```
