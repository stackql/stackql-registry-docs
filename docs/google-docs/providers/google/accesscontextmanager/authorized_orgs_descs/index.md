---
title: authorized_orgs_descs
hide_title: false
hide_table_of_contents: false
keywords:
  - authorized_orgs_descs
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

Creates, updates, deletes, gets or lists a <code>authorized_orgs_descs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorized_orgs_descs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.accesscontextmanager.authorized_orgs_descs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name for the `AuthorizedOrgsDesc`. Format: `accessPolicies/{access_policy}/authorizedOrgsDescs/{authorized_orgs_desc}`. The `authorized_orgs_desc` component must begin with a letter, followed by alphanumeric characters or `_`. After you create an `AuthorizedOrgsDesc`, you cannot change its `name`. |
| <CopyableCode code="assetType" /> | `string` | The asset type of this authorized orgs desc. Valid values are `ASSET_TYPE_DEVICE`, and `ASSET_TYPE_CREDENTIAL_STRENGTH`. |
| <CopyableCode code="authorizationDirection" /> | `string` | The direction of the authorization relationship between this organization and the organizations listed in the `orgs` field. The valid values for this field include the following: `AUTHORIZATION_DIRECTION_FROM`: Allows this organization to evaluate traffic in the organizations listed in the `orgs` field. `AUTHORIZATION_DIRECTION_TO`: Allows the organizations listed in the `orgs` field to evaluate the traffic in this organization. For the authorization relationship to take effect, all of the organizations must authorize and specify the appropriate relationship direction. For example, if organization A authorized organization B and C to evaluate its traffic, by specifying `AUTHORIZATION_DIRECTION_TO` as the authorization direction, organizations B and C must specify `AUTHORIZATION_DIRECTION_FROM` as the authorization direction in their `AuthorizedOrgsDesc` resource. |
| <CopyableCode code="authorizationType" /> | `string` | A granular control type for authorization levels. Valid value is `AUTHORIZATION_TYPE_TRUST`. |
| <CopyableCode code="orgs" /> | `array` | The list of organization ids in this AuthorizedOrgsDesc. Format: `organizations/` Example: `organizations/123456` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accessPoliciesId, authorizedOrgsDescsId" /> | Gets an authorized orgs desc based on the resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accessPoliciesId" /> | Lists all authorized orgs descs for an access policy. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accessPoliciesId" /> | Creates an authorized orgs desc. The long-running operation from this RPC has a successful status after the authorized orgs desc propagates to long-lasting storage. If a authorized orgs desc contains errors, an error response is returned for the first error encountered. The name of this `AuthorizedOrgsDesc` will be assigned during creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accessPoliciesId, authorizedOrgsDescsId" /> | Deletes an authorized orgs desc based on the resource name. The long-running operation from this RPC has a successful status after the authorized orgs desc is removed from long-lasting storage. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="accessPoliciesId, authorizedOrgsDescsId" /> | Updates an authorized orgs desc. The long-running operation from this RPC has a successful status after the authorized orgs desc propagates to long-lasting storage. If a authorized orgs desc contains errors, an error response is returned for the first error encountered. Only the organization list in `AuthorizedOrgsDesc` can be updated. The name, authorization_type, asset_type and authorization_direction cannot be updated. |

## `SELECT` examples

Lists all authorized orgs descs for an access policy.

```sql
SELECT
name,
assetType,
authorizationDirection,
authorizationType,
orgs
FROM google.accesscontextmanager.authorized_orgs_descs
WHERE accessPoliciesId = '{{ accessPoliciesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>authorized_orgs_descs</code> resource.

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
INSERT INTO google.accesscontextmanager.authorized_orgs_descs (
accessPoliciesId,
name,
authorizationType,
assetType,
authorizationDirection,
orgs
)
SELECT 
'{{ accessPoliciesId }}',
'{{ name }}',
'{{ authorizationType }}',
'{{ assetType }}',
'{{ authorizationDirection }}',
'{{ orgs }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
authorizationType: string
assetType: string
authorizationDirection: string
orgs:
  - type: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>authorized_orgs_descs</code> resource.

```sql
/*+ update */
UPDATE google.accesscontextmanager.authorized_orgs_descs
SET 
name = '{{ name }}',
authorizationType = '{{ authorizationType }}',
assetType = '{{ assetType }}',
authorizationDirection = '{{ authorizationDirection }}',
orgs = '{{ orgs }}'
WHERE 
accessPoliciesId = '{{ accessPoliciesId }}'
AND authorizedOrgsDescsId = '{{ authorizedOrgsDescsId }}';
```

## `DELETE` example

Deletes the specified <code>authorized_orgs_descs</code> resource.

```sql
/*+ delete */
DELETE FROM google.accesscontextmanager.authorized_orgs_descs
WHERE accessPoliciesId = '{{ accessPoliciesId }}'
AND authorizedOrgsDescsId = '{{ authorizedOrgsDescsId }}';
```
