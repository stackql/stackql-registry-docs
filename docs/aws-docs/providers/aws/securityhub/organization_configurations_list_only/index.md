---
title: organization_configurations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_configurations_list_only
  - securityhub
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

Lists <code>organization_configurations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/organization_configurations/"><code>organization_configurations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organization_configurations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::OrganizationConfiguration resource represents the configuration of your organization in Security Hub. Only the Security Hub administrator account can create Organization Configuration resource in each region and can opt-in to Central Configuration only in the aggregation region of FindingAggregator.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.organization_configurations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="auto_enable" /></td><td><code>boolean</code></td><td>Whether to automatically enable Security Hub in new member accounts when they join the organization.</td></tr>
<tr><td><CopyableCode code="auto_enable_standards" /></td><td><code>string</code></td><td>Whether to automatically enable Security Hub default standards in new member accounts when they join the organization.</td></tr>
<tr><td><CopyableCode code="configuration_type" /></td><td><code>string</code></td><td>Indicates whether the organization uses local or central configuration.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Describes whether central configuration could be enabled as the ConfigurationType for the organization.</td></tr>
<tr><td><CopyableCode code="status_message" /></td><td><code>string</code></td><td>Provides an explanation if the value of Status is equal to FAILED when ConfigurationType is equal to CENTRAL.</td></tr>
<tr><td><CopyableCode code="member_account_limit_reached" /></td><td><code>boolean</code></td><td>Whether the maximum number of allowed member accounts are already associated with the Security Hub administrator account.</td></tr>
<tr><td><CopyableCode code="organization_configuration_identifier" /></td><td><code>string</code></td><td>The identifier of the OrganizationConfiguration being created and assigned as the unique identifier.</td></tr>
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
Lists all <code>organization_configurations</code> in a region.
```sql
SELECT
region,
organization_configuration_identifier
FROM aws.securityhub.organization_configurations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>organization_configurations_list_only</code> resource, see <a href="/providers/aws/securityhub/organization_configurations/#permissions"><code>organization_configurations</code></a>


