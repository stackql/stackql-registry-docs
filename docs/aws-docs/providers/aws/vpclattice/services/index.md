---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - vpclattice
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

Creates, updates, deletes or gets a <code>service</code> resource or lists <code>services</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A service is any software application that can run on instances containers, or serverless functions within an account or virtual private cloud (VPC).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.services" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auth_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dns_entry" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-service.html"><code>AWS::VpcLattice::Service</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>services</code> in a region.
```sql
SELECT
region,
arn,
auth_type,
created_at,
dns_entry,
id,
last_updated_at,
name,
status,
certificate_arn,
custom_domain_name,
tags
FROM aws.vpclattice.services
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>service</code>.
```sql
SELECT
region,
arn,
auth_type,
created_at,
dns_entry,
id,
last_updated_at,
name,
status,
certificate_arn,
custom_domain_name,
tags
FROM aws.vpclattice.services
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.vpclattice.services (
 AuthType,
 DnsEntry,
 Name,
 CertificateArn,
 CustomDomainName,
 Tags,
 region
)
SELECT 
'{{ AuthType }}',
 '{{ DnsEntry }}',
 '{{ Name }}',
 '{{ CertificateArn }}',
 '{{ CustomDomainName }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.vpclattice.services (
 AuthType,
 DnsEntry,
 Name,
 CertificateArn,
 CustomDomainName,
 Tags,
 region
)
SELECT 
 '{{ AuthType }}',
 '{{ DnsEntry }}',
 '{{ Name }}',
 '{{ CertificateArn }}',
 '{{ CustomDomainName }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: service
    props:
      - name: AuthType
        value: '{{ AuthType }}'
      - name: DnsEntry
        value:
          DomainName: '{{ DomainName }}'
          HostedZoneId: '{{ HostedZoneId }}'
      - name: Name
        value: '{{ Name }}'
      - name: CertificateArn
        value: '{{ CertificateArn }}'
      - name: CustomDomainName
        value: '{{ CustomDomainName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.vpclattice.services
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>services</code> resource, the following permissions are required:

### Create
```json
vpc-lattice:CreateService,
vpc-lattice:GetService,
vpc-lattice:ListTagsForResource,
vpc-lattice:TagResource,
acm:DescribeCertificate,
acm:ListCertificates,
iam:CreateServiceLinkedRole
```

### Read
```json
vpc-lattice:GetService,
vpc-lattice:ListTagsForResource
```

### Update
```json
vpc-lattice:UpdateService,
vpc-lattice:TagResource,
vpc-lattice:UntagResource,
vpc-lattice:GetService,
vpc-lattice:ListTagsForResource
```

### Delete
```json
vpc-lattice:DeleteService,
vpc-lattice:GetService,
vpc-lattice:UntagResource
```

### List
```json
vpc-lattice:ListServices
```
