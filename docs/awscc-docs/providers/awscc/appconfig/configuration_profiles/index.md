---
title: configuration_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_profiles
  - appconfig
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>configuration_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>configuration_profiles</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.appconfig.configuration_profiles</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>application_id</code></td><td><code>string</code></td><td>The application ID.</td></tr>
<tr><td><code>configuration_profile_id</code></td><td><code>string</code></td><td>The configuration profile ID</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>configuration_profiles</code> resource, the following permissions are required:

### Create
<pre>
appconfig:CreateConfigurationProfile,
appconfig:GetConfigurationProfile,
appconfig:TagResource,
appconfig:ListTagsForResource,
iam:PassRole</pre>

### List
<pre>
appconfig:ListConfigurationProfiles</pre>


## Example
```sql
SELECT
region,
application_id,
configuration_profile_id
FROM awscc.appconfig.configuration_profiles
WHERE region = 'us-east-1'
```