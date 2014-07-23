create trigger zombie
instead of delete
on {{table-name}}
for each row
begin
    select 'brains...';
end;
