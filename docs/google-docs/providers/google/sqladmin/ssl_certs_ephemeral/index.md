---
title: ssl_certs_ephemeral
hide_title: false
hide_table_of_contents: false
keywords:
  - ssl_certs_ephemeral
  - sqladmin
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

Creates, updates, deletes, gets or lists a <code>ssl_certs_ephemeral</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ssl_certs_ephemeral</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sqladmin.ssl_certs_ephemeral" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_ephemeral" /> | `INSERT` | <CopyableCode code="instance, project" /> | Generates a short-lived X509 certificate containing the provided public key and signed by a private key specific to the target instance. Users may use the certificate to authenticate as themselves when connecting to the database. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ssl_certs_ephemeral</code> resource.

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
INSERT INTO google.sqladmin.ssl_certs_ephemeral (
instance,
project,
public_key,
access_token
)
SELECT 
'{{ instance }}',
'{{ project }}',
'{{ public_key }}',
'{{ access_token }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: public_key
        value: '{{ public_key }}'
      - name: access_token
        value: '{{ access_token }}'

```
</TabItem>
</Tabs>
