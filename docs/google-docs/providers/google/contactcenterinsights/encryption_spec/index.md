---
title: encryption_spec
hide_title: false
hide_table_of_contents: false
keywords:
  - encryption_spec
  - contactcenterinsights
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

Creates, updates, deletes, gets or lists a <code>encryption_spec</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>encryption_spec</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contactcenterinsights.encryption_spec" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the encryption key specification resource. Format: projects/{project}/locations/{location}/encryptionSpec |
| <CopyableCode code="kmsKey" /> | `string` | Required. The name of customer-managed encryption key that is used to secure a resource and its sub-resources. If empty, the resource is secured by the default Google encryption key. Only the key in the same location as this resource is allowed to be used for encryption. Format: `projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{key}` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_encryption_spec" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Gets location-level encryption key specification. |
| <CopyableCode code="initialize" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Initializes a location-level encryption key specification. An error will be thrown if the location has resources already created before the initialization. Once the encryption specification is initialized at a location, it is immutable and all newly created resources under the location will be encrypted with the existing specification. |

## `SELECT` examples

Gets location-level encryption key specification.

```sql
SELECT
name,
kmsKey
FROM google.contactcenterinsights.encryption_spec
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
