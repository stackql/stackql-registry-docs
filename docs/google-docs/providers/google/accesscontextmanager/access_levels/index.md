---
title: access_levels
hide_title: false
hide_table_of_contents: false
keywords:
  - access_levels
  - accesscontextmanager
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

Creates, updates, deletes, gets or lists a <code>access_levels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_levels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.accesscontextmanager.access_levels" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name for the `AccessLevel`. Format: `accessPolicies/{access_policy}/accessLevels/{access_level}`. The `access_level` component must begin with a letter, followed by alphanumeric characters or `_`. Its maximum length is 50 characters. After you create an `AccessLevel`, you cannot change its `name`. |
| <CopyableCode code="description" /> | `string` | Description of the `AccessLevel` and its use. Does not affect behavior. |
| <CopyableCode code="basic" /> | `object` | `BasicLevel` is an `AccessLevel` using a set of recommended features. |
| <CopyableCode code="custom" /> | `object` | `CustomLevel` is an `AccessLevel` using the Cloud Common Expression Language to represent the necessary conditions for the level to apply to a request. See CEL spec at: https://github.com/google/cel-spec |
| <CopyableCode code="title" /> | `string` | Human readable title. Must be unique within the Policy. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accessLevelsId, accessPoliciesId" /> | Gets an access level based on the resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accessPoliciesId" /> | Lists all access levels for an access policy. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accessPoliciesId" /> | Creates an access level. The long-running operation from this RPC has a successful status after the access level propagates to long-lasting storage. If access levels contain errors, an error response is returned for the first error encountered. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accessLevelsId, accessPoliciesId" /> | Deletes an access level based on the resource name. The long-running operation from this RPC has a successful status after the access level has been removed from long-lasting storage. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="accessLevelsId, accessPoliciesId" /> | Updates an access level. The long-running operation from this RPC has a successful status after the changes to the access level propagate to long-lasting storage. If access levels contain errors, an error response is returned for the first error encountered. |
| <CopyableCode code="replace_all" /> | `REPLACE` | <CopyableCode code="accessPoliciesId" /> | Replaces all existing access levels in an access policy with the access levels provided. This is done atomically. The long-running operation from this RPC has a successful status after all replacements propagate to long-lasting storage. If the replacement contains errors, an error response is returned for the first error encountered. Upon error, the replacement is cancelled, and existing access levels are not affected. The Operation.response field contains ReplaceAccessLevelsResponse. Removing access levels contained in existing service perimeters result in an error. |

## `SELECT` examples

Lists all access levels for an access policy.

```sql
SELECT
name,
description,
basic,
custom,
title
FROM google.accesscontextmanager.access_levels
WHERE accessPoliciesId = '{{ accessPoliciesId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>access_levels</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.accesscontextmanager.access_levels (
accessPoliciesId,
name,
title,
description,
basic,
custom
)
SELECT 
'{{ accessPoliciesId }}',
'{{ name }}',
'{{ title }}',
'{{ description }}',
'{{ basic }}',
'{{ custom }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: title
      value: string
    - name: description
      value: string
    - name: basic
      value:
        - name: conditions
          value:
            - - name: ipSubnetworks
                value:
                  - string
              - name: devicePolicy
                value:
                  - name: requireScreenlock
                    value: boolean
                  - name: allowedEncryptionStatuses
                    value:
                      - string
                  - name: osConstraints
                    value:
                      - - name: osType
                          value: string
                        - name: minimumVersion
                          value: string
                        - name: requireVerifiedChromeOs
                          value: boolean
                  - name: allowedDeviceManagementLevels
                    value:
                      - string
                  - name: requireAdminApproval
                    value: boolean
                  - name: requireCorpOwned
                    value: boolean
              - name: requiredAccessLevels
                value:
                  - string
              - name: negate
                value: boolean
              - name: members
                value:
                  - string
              - name: regions
                value:
                  - string
              - name: vpcNetworkSources
                value:
                  - - name: vpcSubnetwork
                      value:
                        - name: network
                          value: string
                        - name: vpcIpSubnetworks
                          value:
                            - string
        - name: combiningFunction
          value: string
    - name: custom
      value:
        - name: expr
          value:
            - name: expression
              value: string
            - name: title
              value: string
            - name: description
              value: string
            - name: location
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>access_levels</code> resource.

```sql
/*+ update */
UPDATE google.accesscontextmanager.access_levels
SET 
name = '{{ name }}',
title = '{{ title }}',
description = '{{ description }}',
basic = '{{ basic }}',
custom = '{{ custom }}'
WHERE 
accessLevelsId = '{{ accessLevelsId }}'
AND accessPoliciesId = '{{ accessPoliciesId }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>access_levels</code> resource.

```sql
/*+ update */
REPLACE google.accesscontextmanager.access_levels
SET 
accessLevels = '{{ accessLevels }}',
etag = '{{ etag }}'
WHERE 
accessPoliciesId = '{{ accessPoliciesId }}';
```

## `DELETE` example

Deletes the specified <code>access_levels</code> resource.

```sql
/*+ delete */
DELETE FROM google.accesscontextmanager.access_levels
WHERE accessLevelsId = '{{ accessLevelsId }}'
AND accessPoliciesId = '{{ accessPoliciesId }}';
```
