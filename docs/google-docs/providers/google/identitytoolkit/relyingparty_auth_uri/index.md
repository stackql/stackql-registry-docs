---
title: relyingparty_auth_uri
hide_title: false
hide_table_of_contents: false
keywords:
  - relyingparty_auth_uri
  - identitytoolkit
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

Creates, updates, deletes, gets or lists a <code>relyingparty_auth_uri</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>relyingparty_auth_uri</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.identitytoolkit.relyingparty_auth_uri" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_auth_uri" /> | `INSERT` | <CopyableCode code="" /> | Creates the URI used by the IdP to authenticate the user. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>relyingparty_auth_uri</code> resource.

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
INSERT INTO google.identitytoolkit.relyingparty_auth_uri (
,
appId,
authFlowType,
clientId,
context,
continueUri,
customParameter,
hostedDomain,
identifier,
oauthConsumerKey,
oauthScope,
openidRealm,
otaApp,
providerId,
sessionId,
tenantId,
tenantProjectNumber
)
SELECT 
'{{  }}',
'{{ appId }}',
'{{ authFlowType }}',
'{{ clientId }}',
'{{ context }}',
'{{ continueUri }}',
'{{ customParameter }}',
'{{ hostedDomain }}',
'{{ identifier }}',
'{{ oauthConsumerKey }}',
'{{ oauthScope }}',
'{{ openidRealm }}',
'{{ otaApp }}',
'{{ providerId }}',
'{{ sessionId }}',
'{{ tenantId }}',
'{{ tenantProjectNumber }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
appId: string
authFlowType: string
clientId: string
context: string
continueUri: string
customParameter: object
hostedDomain: string
identifier: string
oauthConsumerKey: string
oauthScope: string
openidRealm: string
otaApp: string
providerId: string
sessionId: string
tenantId: string
tenantProjectNumber: string

```
</TabItem>
</Tabs>
