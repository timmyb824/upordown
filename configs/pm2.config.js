module.exports = {
    apps : [
    {
        name: 'upordown',
        script: ' gunicorn main:app -w 2 --bind 127.0.0.1:5001; ',
        cwd: '/Users/timothybryant/DevOps-Personal/git-personal/upordown/src', //mac
        // cwd: '/home/tbryant/DevOps-WSL/gitea/upordown/src', //WSL
        watch: false,
        // args: 'one two',
        // merge_logs: true,
        // autorestart: true,
        // log_file: "logs/combined.outerr.log",
        // out_file: "logs/out.log",
        // error_file: "logs/err.log",
        // log_date_format : "YYYY-MM-DD HH:mm Z",
        // append_env_to_name: true,
        // interpreter: "/Users/timothybryant/.pyenv/versions/3.10.1/envs/upordown/bin/python",
        // max_memory_restart: '5G',
    },
  ],
};