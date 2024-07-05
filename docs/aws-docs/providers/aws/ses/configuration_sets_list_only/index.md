---
title: configuration_sets_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_sets_list_only
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

Lists <code>configuration_sets</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/configuration_sets/"><code>configuration_sets</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_sets_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::SES::ConfigurationSet.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ses.configuration_sets_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the configuration set.</td></tr>
<tr><td><CopyableCode code="tracking_options" /></td><td><code>object</code></td><td>An object that defines the open and click tracking options for emails that you send using the configuration set.</td></tr>
<tr><td><CopyableCode code="delivery_options" /></td><td><code>object</code></td><td>An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.</td></tr>
<tr><td><CopyableCode code="reputation_options" /></td><td><code>object</code></td><td>An object that defines whether or not Amazon SES collects reputation metrics for the emails that you send that use the configuration set.</td></tr>
<tr><td><CopyableCode code="sending_options" /></td><td><code>object</code></td><td>An object that defines whether or not Amazon SES can send email that you send using the configuration set.</td></tr>
<tr><td><CopyableCode code="suppression_options" /></td><td><code>object</code></td><td>An object that contains information about the suppression list preferences for your account.</td></tr>
<tr><td><CopyableCode code="vdm_options" /></td><td><code>object</code></td><td>An object that contains Virtual Deliverability Manager (VDM) settings for this configuration set.</td></tr>
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
Lists all <code>configuration_sets</code> in a region.
```sql
SELECT
region,
name
FROM aws.ses.configuration_sets_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>configuration_sets_list_only</code> resource, see <a href="/providers/aws/ses/configuration_sets/#permissions"><code>configuration_sets</code></a>


