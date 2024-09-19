---
title: inbound_saml_sso_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - inbound_saml_sso_profiles
  - cloudidentity
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

Creates, updates, deletes, gets or lists a <code>inbound_saml_sso_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inbound_saml_sso_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudidentity.inbound_saml_sso_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the SAML SSO profile. |
| <CopyableCode code="customer" /> | `string` | Immutable. The customer. For example: `customers/C0123abc`. |
| <CopyableCode code="displayName" /> | `string` | Human-readable name of the SAML SSO profile. |
| <CopyableCode code="idpConfig" /> | `object` | SAML IDP (identity provider) configuration. |
| <CopyableCode code="spConfig" /> | `object` | SAML SP (service provider) configuration. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="inboundSamlSsoProfilesId" /> | Gets an InboundSamlSsoProfile. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists InboundSamlSsoProfiles for a customer. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="" /> | Creates an InboundSamlSsoProfile for a customer. When the target customer has enabled [Multi-party approval for sensitive actions](https://support.google.com/a/answer/13790448), the `Operation` in the response will have `"done": false`, it will not have a response, and the metadata will have `"state": "awaiting-multi-party-approval"`. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="inboundSamlSsoProfilesId" /> | Deletes an InboundSamlSsoProfile. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="inboundSamlSsoProfilesId" /> | Updates an InboundSamlSsoProfile. When the target customer has enabled [Multi-party approval for sensitive actions](https://support.google.com/a/answer/13790448), the `Operation` in the response will have `"done": false`, it will not have a response, and the metadata will have `"state": "awaiting-multi-party-approval"`. |

## `SELECT` examples

Lists InboundSamlSsoProfiles for a customer.

```sql
SELECT
name,
customer,
displayName,
idpConfig,
spConfig
FROM google.cloudidentity.inbound_saml_sso_profiles
;
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>inbound_saml_sso_profiles</code> resource.

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
INSERT INTO google.cloudidentity.inbound_saml_sso_profiles (
customer,
displayName,
idpConfig,
spConfig
)
SELECT 
'{{ customer }}',
'{{ displayName }}',
'{{ idpConfig }}',
'{{ spConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: customer
      value: string
    - name: displayName
      value: string
    - name: idpConfig
      value:
        - name: entityId
          value: string
        - name: singleSignOnServiceUri
          value: string
        - name: logoutRedirectUri
          value: string
        - name: changePasswordUri
          value: string
    - name: spConfig
      value:
        - name: entityId
          value: string
        - name: assertionConsumerServiceUri
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>inbound_saml_sso_profiles</code> resource.

```sql
/*+ update */
UPDATE google.cloudidentity.inbound_saml_sso_profiles
SET 
customer = '{{ customer }}',
displayName = '{{ displayName }}',
idpConfig = '{{ idpConfig }}',
spConfig = '{{ spConfig }}'
WHERE 
inboundSamlSsoProfilesId = '{{ inboundSamlSsoProfilesId }}';
```

## `DELETE` example

Deletes the specified <code>inbound_saml_sso_profiles</code> resource.

```sql
/*+ delete */
DELETE FROM google.cloudidentity.inbound_saml_sso_profiles
WHERE inboundSamlSsoProfilesId = '{{ inboundSamlSsoProfilesId }}';
```
