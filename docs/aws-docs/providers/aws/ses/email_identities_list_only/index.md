---
title: email_identities_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - email_identities_list_only
  - ses
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>email_identities</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/email_identities/"><code>email_identities</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>email_identities_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SES::EmailIdentity</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ses.email_identities_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="email_identity" /></td><td><code>string</code></td><td>The email address or domain to verify.</td></tr>
<tr><td><CopyableCode code="configuration_set_attributes" /></td><td><code>object</code></td><td>Used to associate a configuration set with an email identity.</td></tr>
<tr><td><CopyableCode code="dkim_signing_attributes" /></td><td><code>object</code></td><td>If your request includes this object, Amazon SES configures the identity to use Bring Your Own DKIM (BYODKIM) for DKIM authentication purposes, or, configures the key length to be used for Easy DKIM.</td></tr>
<tr><td><CopyableCode code="dkim_attributes" /></td><td><code>object</code></td><td>Used to enable or disable DKIM authentication for an email identity.</td></tr>
<tr><td><CopyableCode code="mail_from_attributes" /></td><td><code>object</code></td><td>Used to enable or disable the custom Mail-From domain configuration for an email identity.</td></tr>
<tr><td><CopyableCode code="feedback_attributes" /></td><td><code>object</code></td><td>Used to enable or disable feedback forwarding for an identity.</td></tr>
<tr><td><CopyableCode code="dkim_dns_token_name1" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dkim_dns_token_name2" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dkim_dns_token_name3" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dkim_dns_token_value1" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dkim_dns_token_value2" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dkim_dns_token_value3" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>email_identities</code> in a region.
```sql
SELECT
region,
email_identity
FROM aws.ses.email_identities_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>email_identities_list_only</code> resource, see <a href="/providers/aws/ses/email_identities/#permissions"><code>email_identities</code></a>


